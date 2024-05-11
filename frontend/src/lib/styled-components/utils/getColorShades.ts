import Color from 'color';

import { IColorShades } from '../theme/types/color.type';

export function getColorShades(
    color_: string,
    primaryDelta: number,
    secondaryDelta: number,
): IColorShades {
    const color = Color(color_);
    const { h, s, l, alpha = 100 } = color.hsl().object();

    const colors: IColorShades = {
        major: {
            normal: '',
            hover: '',
        },
        minor: {
            normal: '',
            hover: '',
        },
    };

    if (color.isLight()) {
        colors.major = {
            normal: Color({ h, s, l, alpha }).toString(),
            hover: Color({ h, s, l: l - primaryDelta, alpha }).toString(),
        };
        colors.minor = {
            normal: Color({ h, s, l: l - secondaryDelta, alpha }).toString(),
            hover: Color({ h, s, l: l - primaryDelta - secondaryDelta, alpha }).toString(), // prettier-ignore
        };
    } else {
        colors.major = {
            normal: Color({ h, s, l, alpha }).toString(),
            hover: Color({ h, s, l: l + primaryDelta, alpha }).toString(),
        };
        colors.minor = {
            normal: Color({ h, s, l: l + secondaryDelta, alpha }).toString(),
            hover: Color({ h, s, l: l + primaryDelta + secondaryDelta, alpha }).toString(), // prettier-ignore
        };
    }

    return colors;
}
