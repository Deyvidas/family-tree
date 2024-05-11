import { getColorShades } from '../utils/getColorShades';
import { ThemeSharedValues } from './shared';
import { IColorCategories } from './types/color.type';
import { ITheme } from './types/final.type';

const ThemeLightValues: IColorCategories = {
    app: getColorShades('hsl(0, 0.00%, 92.20%)', 10, 40),
    primary: getColorShades('hsl(0, 0.00%, 7%)', 30, 60),
    secondary: getColorShades('hsl(14, 94.30%, 48.40%)', 10, 40),
    error: getColorShades('hsl(0, 93.60%, 48.80%)', 10, 40),
    warning: getColorShades('hsl(46, 93.60%, 49.20%)', 10, 40),
    info: getColorShades('hsl(216, 92.80%, 48.80%)', 10, 40),
    success: getColorShades('hsl(118, 92.40%, 25.70%)', 10, 40),
};

export const ThemeLight: ITheme = {
    ...ThemeSharedValues,
    color: ThemeLightValues,
};
