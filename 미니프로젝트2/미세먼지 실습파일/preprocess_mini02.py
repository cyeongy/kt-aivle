from datetime import datetime, timedelta
import pandas as pd


def trans_datetime(temp):
    if '측정일시' in list(temp.columns):
        temp.rename(columns={'측정일시': '일시'}, inplace=True)

    if temp['일시'].dtype == "datetime64[ns]":
        return
    try:
        temp['일시'] = temp['일시'].apply(lambda x: pd.to_datetime(str(x)[:8], format='%Y%m%d') + (
            timedelta(days=1, hours=0) if x % 100 == 24 else timedelta(hours=x % 100)))
    except:
        temp['일시'] = temp['일시'].apply(lambda x: pd.to_datetime(x))


def __drop_ground_condition(weather):
    """
    지면상태(지면상태코드)는 전부 NaN이므로 예측에 사용할 수 없음.
    :param weather: DataFrame
    :return: None (데이터프레임 자체를 수정)
    """

    if '지면상태(지면상태코드)' in list(weather.columns):
        weather.drop('지면상태(지면상태코드)', axis=1, inplace=True)


def __fill_QC_flag_zero(weather):
    """
    QC 플래그 NaN -> 0
    :param weather: DataFrame
    :return: None (데이터프레임 자체를 수정)
    """
    for col in weather.filter(like='QC'):
        weather[col].fillna(0, inplace=True)


def __trans_nan_to_zero(weather):
    """
    강수량의 NaN 플래그는 비가 오지 않은 것. 0mm로 변환
    일조(hr)과 일사(MJ/m2)의 결측치와 QC플래그는 서로 배타 관계. 즉 일출, 일몰 여부이므로 NaN -> 0
    적설(cm)와 3시간신적설(cm)의 관측값은 12월에서 3월 사이에 종종 나타남. NaN은 눈이 오지 않은 것임을 알 수 있음.
    :param weather: DataFrame : weather
    :return: None (데이터프레임 자체를 수정)
    """
    for col in ['강수량(mm)', '일조(hr)', '일사(MJ/m2)', '적설(cm)']:
        if col in list(weather.columns):
            weather[col].fillna(0, inplace=True)


def __fill_snow_3hours(weather):
    weather['3hours'] = weather['적설(cm)'].diff(3)
    weather.loc[weather['3시간신적설(cm)'].isna(), '3시간신적설(cm)'] = weather.loc[weather['3시간신적설(cm)'].isna(), '3hours']
    weather.loc[:3, '3시간신적설(cm)'] = weather.loc[:3, '적설(cm)']
    weather.drop(columns='3hours', inplace=True)


def __fill_temp_interpolate(weather):
    temp = weather.loc[:, ['일시', '지면온도(°C)', '5cm 지중온도(°C)', '10cm 지중온도(°C)', '20cm 지중온도(°C)', '30cm 지중온도(°C)']]
    temp = temp.set_index('일시').interpolate()
    temp = temp.reset_index()
    weather[['지면온도(°C)', '5cm 지중온도(°C)', '10cm 지중온도(°C)', '20cm 지중온도(°C)', '30cm 지중온도(°C)']] = temp[
        ['지면온도(°C)', '5cm 지중온도(°C)', '10cm 지중온도(°C)', '20cm 지중온도(°C)', '30cm 지중온도(°C)']]


def __fill_wind_interpolate(weather):
    temp = weather.loc[:, ['일시', '풍속(m/s)', '풍향(16방위)']]
    temp = temp.set_index('일시').interpolate()
    temp = temp.reset_index()
    weather[['풍속(m/s)', '풍향(16방위)']] = temp[['풍속(m/s)', '풍향(16방위)']]


def __rename_to_is_sun_rised(weather):
    if '일사 QC플래그' in list(weather.columns):
        weather.rename(columns={'일사 QC플래그': '일몰 여부'}, inplace=True)
    weather.drop(columns=weather.filter(like='QC').columns, inplace=True)


def __make_climate_code_dummies(weather):
    if '현상번호(0)' in list(weather.columns):
        return
    for i in [0, 1, 2, 4, 5, 6, 10, 11, 16, 19, 40, 42]:
        weather[f'현상번호({i})'] = 0
    for _idx, _row in weather.iterrows():
        if _row.isna()['현상번호(국내식)']:
            weather['현상번호(0)'] = 1
            continue

        _number = int(_row['현상번호(국내식)'])
        while _number != 0:
            _key = _number % 100
            _number = _number // 100
            if _key not in [1, 2, 4, 5, 6, 10, 11, 16, 19, 40, 42]:
                assert f"Weather 데이터프레임에서 미확인 현상번호({_key}) 발견"
                continue
            weather.loc[_idx, f'현상번호({_key})'] = 1

    weather.drop(columns=['현상번호(국내식)'], axis=1, inplace=True)


def __fill_cloud_volume(temp):
    if '운형(운형약어)' not in temp.columns:
        return
    __var = temp.loc[temp['운형(운형약어)'].isna(), '전운량(10분위)'].mode()[0]
    temp.loc[temp['전운량(10분위)'].isna() & temp['운형(운형약어)'].isna(), '전운량(10분위)'] = __var

    __var = temp.loc[temp['운형(운형약어)'].isna(), '중하층운량(10분위)'].mode()[0]
    temp.loc[temp['중하층운량(10분위)'].isna() & temp['운형(운형약어)'].isna(), '중하층운량(10분위)'] = __var

    __var = temp.loc[~temp['운형(운형약어)'].isna(), '전운량(10분위)'].mode()[0]
    temp.loc[temp['전운량(10분위)'].isna() & ~temp['운형(운형약어)'].isna(), '전운량(10분위)'] = __var

    __var = temp.loc[~temp['운형(운형약어)'].isna(), '중하층운량(10분위)'].mode()[0]
    temp.loc[temp['중하층운량(10분위)'].isna() & ~temp['운형(운형약어)'].isna(), '중하층운량(10분위)'] = __var


def __make_cloud_form_dummies(temp):
    if '운형(Ci)' in list(temp.columns):
        return

    for form in ['운형(Ci)', '운형(Cc)', '운형(Cs)', '운형(Ac)', '운형(As)', '운형(Ns)', '운형(Sc)', '운형(St)', '운형(Cu)',
                 '운형(Cb)']:
        temp[form] = 0

    for _idx, _row in temp.iterrows():
        if _row.isna()['운형(운형약어)']:
            continue

        __text = _row['운형(운형약어)']
        for __i in range(0, len(__text), 2):
            temp.loc[_idx, f'운형({__text[__i:__i + 2]})'] = 1

    temp.drop(columns=['운형(운형약어)'], axis=1, inplace=True)


def __fill_cloud_low(temp):
    temp.drop(columns=['최저운고(100m )'], inplace=True)


def fill_weather(weather):
    '''
    weather 변수 전처리 함수
    :param weather: DataFrame
    :return: None (데이터프레임 자체를 수정)
    '''

    # 지면상태(지면상태코드)는 전부 NaN이므로 예측에 사용할 수 없음.
    __drop_ground_condition(weather)

    # QC 플래그 NaN -> 0
    __fill_QC_flag_zero(weather)

    # 강수량의 NaN 플래그는 비가 오지 않은 것. 0mm로 변환
    # 일조(hr)과 일사(MJ/m2)의 결측치와 QC플래그는 서로 배타 관계. 즉 일출, 일몰 여부이므로 NaN -> 0
    # 적설(cm)와 3시간신적설(cm)의 관측값은 12월에서 3월 사이에 종종 나타남. NaN은 눈이 오지 않은 것임을 알 수 있음.
    __trans_nan_to_zero(weather)

    # 다만 3시간신적설(cm)의 경우 3시간(3칸) 마다 기록하므로 그 사이 결측치를 0으로 채우는 것은 무리가 있음.
    # 3가지로 나누어 생각 해 볼 수 있음
    # 1. 단위시간당 적설로 바꾼다. : 단위 시간당 적설량으로 바꾸어 3시간신적설(cm)/3 을 하여 균등 기록한다.
    # 2. bfill : NaN 두칸을 3시간 단위의 적설량과 동일하게 채운다.
    # 3. 적설(cm)의 데이터를 diff(3)를 한다.

    # 3번 가설 적용
    __fill_snow_3hours(weather)

    # 지면 온도와 지중온도의 결측치는 굉장히 시간에 따라 증감을 반복하는 모양이 반복된다.
    # 짧은 시간이라면 시간에 따라 정렬 후 interploate(method='linear')를 하고, 하루 이상의 긴 시간이라면 시간에 따른 변수를 중점적으로 두고 전날이나 다음날의 온도를 복사하는 것이 좋겠다
    __fill_temp_interpolate(weather)

    # 풍속 또한 임의로 시간에 따라 interpolate한다. 추후 다른 Imputer를 사용한다
    __fill_wind_interpolate(weather)

    # 모든 QC플래그(관측, 결측 여부)의 결측치 보충 끝. 일조, 일사 플래그 중 하나를 일몰 여부로 바꾸로 나머지 QC 플래그는 모두 drop
    __rename_to_is_sun_rised(weather)

    # 현상번호(국내식)은 날씨의 코드를 큰 순서부터 두자리씩 잘라서 이어붙인 코드. 국내 코드가 여럿 있지만 다른 것은 보이지 않는다. train set에는 이것만 있으니 이 종류만 가변수화한다.
    # 다만 미래의 test set에 추가로 발견된다면 어떻게 처리할지 생각해보아야함.
    # NaN 0 맑음
    # 19 박무
    # 1 비
    # 40 연무
    # 42 황사
    # 5 눈
    # 4 소낙비
    # 10 싸락눈
    # 11 가루눈
    # 6 진눈깨비
    # 16 안개, 낮은안개
    # 2 이슬비
    # [0, 1, 2, 4, 5, 6, 10, 11, 16, 19, 40, 42]
    __make_climate_code_dummies(weather)

    # 전운량과 중하층운량은 운형(운형약어)의 유무에 따라 굉장히 큰 차이가 난다. 최빈값으로 넣어준다.
    # 운형 가변수화 전에 꼭 들어가야함
    __fill_cloud_volume(weather)

    # 운형의 경우 사람이 직접 관측하고 발표하기 떄문에 야간의 관측 기록이 상당히 적음.
    # 대부분 주간에 발표 되어있으나 이 경우 야간에 관측을 했던 날의 날씨가 어떠했는지 알아볼 필요가 있음.
    # 운형의 경우 더미화 진행. 운형(운형약어)는 삭제
    # ['운형(Ci)',  # 상층 - 권운
    #  '운형(Cc)',  # 상층 - 권적운
    #  '운형(Cs)',  # 상층 - 권층운
    #  '운형(Ac)',  # 중층 - 고적운
    #  '운형(As)',  # 중층 - 고층운
    #  '운형(Ns)',  # 중층 - 난층운
    #  '운형(Sc)',  # 하층 - 층적운
    #  '운형(St)',  # 하층 - 층운
    #  '운형(Cu)',  # 하층 - 적운
    #  '운형(Cb)']  # 하층 - 적란운
    __make_cloud_form_dummies(weather)

    # 최저운고(100m )의 경우는 하층 운형에 따라 영향을 크게 받는 듯하다. 이건 회귀 분석 후에 보충할 것, 결측치가 많은 만큼 잠시 drop한다.
    __fill_cloud_low(weather)
