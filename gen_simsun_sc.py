import utils
import shutil as fs

def gen_simsun_sc(path):
    fs.copy(path + '/SarasaUiSC-Regular.ttf', path + '/SarasaUiSC-Regular-new.ttf')

    font = utils.open_font(path + '/SarasaUiSC-Regular.ttf')
    utils.remove_gasp(font)
    utils.set_cleartype(font)
    utils.set_simsun_names(font)

    font_ui = utils.open_font(path + '/SarasaUiSC-Regular-new.ttf')
    utils.remove_gasp(font_ui)
    utils.set_cleartype(font_ui)
    utils.set_new_simsun_names(font_ui)

    font.generateTtc(path + '/simsun.ttc', font_ui, ttcflags = ('merge'), layer = 1)

def gen_simsun_ext_sc(path):
    font = utils.open_font(path + '/SarasaUiSC-Regular.ttf')
    utils.remove_gasp(font)
    utils.set_cleartype(font)
    utils.set_simsun_ext_names(font)

    font.generate(path + '/simsunb.ttf')
