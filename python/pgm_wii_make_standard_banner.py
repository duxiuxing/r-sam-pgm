# -- coding: UTF-8 --

from wii_make_standard_banner import S_BannerInfo, Wii_MakeStandardBanner


if __name__ == "__main__":
    kov_logo_size = (150, 48)
    kov_banner_info = S_BannerInfo(
        "kov",
        game_logo_size=kov_logo_size,
        game_logo_left_top=S_BannerInfo.compute_logo_left_top(
            kov_logo_size, S_BannerInfo.ALIGN_RIGHT_TOP
        ),
        console_logo_align=S_BannerInfo.ALIGN_RIGHT_BOTTOM,
    )

    kovplus_logo_size = (200, 78)
    kovplus_banner_info = S_BannerInfo(
        "kovplus",
        game_logo_size=kovplus_logo_size,
        game_logo_left_top=S_BannerInfo.compute_logo_left_top(
            kovplus_logo_size, S_BannerInfo.ALIGN_RIGHT_TOP
        ),
        console_logo_align=S_BannerInfo.ALIGN_RIGHT_BOTTOM,
    )
    Wii_MakeStandardBanner(kovplus_banner_info).run()
