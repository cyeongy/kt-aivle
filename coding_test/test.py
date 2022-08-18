import matplotlib.pyplot as plt
import matplotlib as mpl

# 가능한 font list 확인
import matplotlib.font_manager as fm
f = [f.name for f in fm.fontManager.ttflist]
print(f)
print(mpl.get_configdir())

# 확인 이후
plt.rc('font', family='Malgun Gothic')

fm.findSystemFonts()