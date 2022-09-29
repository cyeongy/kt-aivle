def Load_image(image_path):
    """
    이미지를 불러오는 함수, 이미지(확장자 존재 .jpg, .png)를 입력\n
    :param image_path: 이미지  경로
    :return: 이미지
    """
    import cv2
    import numpy as np
    # image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

    image = cv2.imdecode(np.fromfile(image_path, np.uint8), cv2.IMREAD_UNCHANGED)
    return image


def Crop_image(image, title=True):
    """
    이미지를 크롭하는 함수
    :param image: 원본 이미지
    :param title: 코미디빅리그 타이틀 포함 유무, 기본은 포함
    :return: image: 크롭 된 이미지:cv2(BGR)
    """
    if title:
        _image = image[0:120, 0:200]
    else:
        _image = image[58:58 + 17, 50:50 + 95]

    return _image


def Sharp_image(image):
    import cv2
    import numpy as np

    sharpening_mask2 = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    image_sharp = cv2.filter2D(image, -1, sharpening_mask2)

    return image_sharp


def Convert_gray_image(image):
    """
    cv2(BGR) -> image(Gray)\n
    :param image: 입력 이미지(cv2, BGR)
    :return image: 그레이 스케일 이미지
    """
    import cv2

    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def Detect_edge(image):
    """
    이미지에 캐니필터 적용\n
    :param image: 원본 이미지
    :return _image: Canny Filter를 적용한 이미지
    """
    import cv2

    _image = cv2.Canny(image, 100, 255)

    return _image


def MakeGrayScale(FilePath):
    import glob, cv2, sys, os

    image_list = glob.glob(FilePath + "/*.png")
    for image in image_list:

        src = cv2.imread(image, cv2.IMREAD_GRAYSCALE)

        if src is None:
            print('Image load failed!')
            sys.exit()

        if not os.path.exists(FilePath + "/gray"):
            os.mkdir(FilePath + "/gray")
        cv2.imwrite(FilePath + "/gray/" + image.split(":")[-1], src)


def MakeEdgeDetection(FilePath):
    import glob, cv2, sys, os
    image_list = glob.glob(FilePath + "/*.png")
    for image in image_list:

        src = cv2.imread(image, cv2.IMREAD_GRAYSCALE)

        if src is None:
            print('Image load failed!')
            sys.exit()

        if not os.path.exists(FilePath + "/edge"):
            os.mkdir(FilePath + "/edge")

        dst = cv2.Canny(src, 100, 255)

        cv2.imwrite(FilePath + "/edge/" + image.split(":")[-1], dst)


def Make_image(src_path, dst_path, title, gray, sharp, edge):
    """
    :param src_path: 전처리 이전 데이터 경로
    :param dst_path: 전처리 데이터 저장 경로
    :param title: 크롭 이미지 타이틀 포함 유무
    :param gray: 그레이 변환 유무
    :param sharp: 샤프닝 유무
    :param edge: 엣지 검출 유무
    :return:
    """
    import os, glob, cv2
    from collections import defaultdict

    image_list = glob.glob(os.path.join(src_path, '*.jpg'))
    images = []
    for path in image_list:
        images.append(Load_image(path))

    images = [Crop_image(image, title) for image in images]
    if gray:
        images = [Convert_gray_image(image) for image in images]
    if sharp:
        images = [Sharp_image(image) for image in images]
    if edge:
        images = [Detect_edge(image) for image in images]

    for idx, image in enumerate(images):
        # cv2.imwrite(os.path.join(dst_path, f'{idx}.jpg'), image)

        ret, img = cv2.imencode('.jpg', image)
        with open(os.path.join(dst_path, f'{idx}.jpg'), 'w+b') as f:
            img.tofile(f)
    return


if __name__ == '__main__':
    import os, glob, cv2, numpy as np

    ROOT_PATH = os.path.abspath('..')
    VIDEO_PATH = os.path.join(ROOT_PATH, 'video')

    keys = {'title': True,
            'gray': True,
            'sharp': True,
            'edge': False}

    Make_image(os.path.join(ROOT_PATH, 'train'), os.path.join(VIDEO_PATH, 'temp'), True, True, True, False)

    # print(glob.glob(os.path.join(ROOT_PATH, 'train', '*.jpg')))
