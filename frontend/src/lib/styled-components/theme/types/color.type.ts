export type AppThemes = 'dark' | 'light';

export interface IColorCategories {
    app: IColorShades;
    primary: IColorShades;
    secondary: IColorShades;
    error: IColorShades;
    warning: IColorShades;
    info: IColorShades;
    success: IColorShades;
}

export interface IColorShades {
    major: {
        normal: string;
        hover: string;
    };
    minor: {
        normal: string;
        hover: string;
    };
}
