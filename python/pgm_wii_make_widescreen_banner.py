# -- coding: UTF-8 --

from wii_make_widescreen_banner import W_BannerInfo, Wii_MakeWidescreenBanner


if __name__ == "__main__":
    kov_banner_info = W_BannerInfo(
        "kov",
        game_logo_size=(0, 0),
        game_logo_left_top=(0, 0),
        console_logo_align=W_BannerInfo.ALIGN_RIGHT_BOTTOM,
    )

    kovplus_logo_size = (204, 80)
    kovplus_banner_info = W_BannerInfo(
        "kovplus",
        game_logo_size=kovplus_logo_size,
        game_logo_left_top=W_BannerInfo.compute_logo_left_top(
            kovplus_logo_size, W_BannerInfo.ALIGN_TOP_CENTER
        ),
        console_logo_align=W_BannerInfo.ALIGN_RIGHT_BOTTOM,
    )
    Wii_MakeWidescreenBanner(kovplus_banner_info).run()
