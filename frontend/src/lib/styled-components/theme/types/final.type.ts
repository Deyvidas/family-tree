import { IColorCategories } from './color.type';
import { ISharedThemeAttributes } from './shared.type';

export interface ITheme extends ISharedThemeAttributes {
    color: IColorCategories;
}
