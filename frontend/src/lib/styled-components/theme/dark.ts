import { getColorShades } from '../utils/getColorShades';
import { ThemeSharedValues } from './shared';
import { IColorCategories } from './types/color.type';
import { ITheme } from './types/final.type';

const ThemeDarkValues: IColorCategories = {
    app: getColorShades('hsl(0, 0.00%, 7%)', 10, 40),
    primary: getColorShades('hsl(0, 4.90%, 88.00%)', 30, 60),
    secondary: getColorShades('hsl(32, 99%, 51.40%)', 20, 40),
    error: getColorShades('hsl(0, 93.60%, 48.80%)', 10, 40),
    warning: getColorShades('hsl(46, 93.60%, 49.20%)', 10, 40),
    info: getColorShades('hsl(216, 92.80%, 48.80%)', 10, 40),
    success: getColorShades('hsl(118, 92.40%, 25.70%)', 10, 40),
};

export const ThemeDark: ITheme = {
    ...ThemeSharedValues,
    color: ThemeDarkValues,
};
