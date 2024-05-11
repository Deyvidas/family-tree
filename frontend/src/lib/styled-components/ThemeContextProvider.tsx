'use client';

import R from 'react';

import { AppThemes } from './theme/types/color.type';

export interface IThemeContext {
    theme: AppThemes;
    setTheme: R.Dispatch<R.SetStateAction<AppThemes>>;
}

export const ThemeContext = R.createContext<IThemeContext>({
    theme: 'dark',
    setTheme: () => {},
});

/**
 * Context allows to detect the theme state from all parts of the app that are in this
 * context.
 */
export function ThemeContextProvider({ children }: R.PropsWithChildren) {
    const [theme, setTheme] = R.useState<AppThemes>('dark');
    const value: IThemeContext = { theme, setTheme };

    return <ThemeContext.Provider value={value}>{children}</ThemeContext.Provider>;
}
