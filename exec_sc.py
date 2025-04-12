import utils, gen_yahei_sc, gen_simsun_sc

if __name__ == '__main__':

    gen_yahei_sc.gen_yahei_regular_sc(utils.DIR_HINTED)
    gen_yahei_sc.gen_yahei_bold_sc(utils.DIR_HINTED)
    gen_yahei_sc.gen_yahei_light_sc(utils.DIR_HINTED)
    print('hinted yahei successfully generated')

    gen_simsun_sc.gen_simsun_sc(utils.DIR_HINTED)
    gen_simsun_sc.gen_simsun_ext_sc(utils.DIR_HINTED)
    print('hinted simsun successfully generated')

    gen_yahei_sc.gen_yahei_regular_sc(utils.DIR_UNHINTED)
    gen_yahei_sc.gen_yahei_bold_sc(utils.DIR_UNHINTED)
    gen_yahei_sc.gen_yahei_light_sc(utils.DIR_UNHINTED)
    print('unhinted yahei successfully generated')

    gen_simsun_sc.gen_simsun_sc(utils.DIR_UNHINTED)
    gen_simsun_sc.gen_simsun_ext_sc(utils.DIR_UNHINTED)
    print('unhinted simsun successfully generated')

