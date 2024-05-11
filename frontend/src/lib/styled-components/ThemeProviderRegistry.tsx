'use client';

import R from 'react';
import { ThemeProvider, createGlobalStyle } from 'styled-components';

import { ThemeContext } from './ThemeContextProvider';
import { ThemeDark } from './theme/dark';
import { ThemeLight } from './theme/light';
import { AppThemes } from './theme/types/color.type';
import { ITheme } from './theme/types/final.type';

type IThemes = {
    [key in AppThemes]: ITheme;
};

const Themes: IThemes = {
    dark: ThemeDark,
    light: ThemeLight,
};

const GlobalStyle = createGlobalStyle`
    html {
        height: 100%;
        overflow-y: auto;

        font-family: ${p => p.theme.global.typography.fontFamily};
        font-size: ${p => p.theme.global.typography.fontSize};
        font-weight: ${p => p.theme.global.typography.fontWeight};
        line-height: ${p => p.theme.global.typography.lineHeight};

        scroll-behavior: smooth;

        * {
            line-height: ${p => p.theme.global.typography.lineHeight};
        }
    }

    body {
        height: 100%;
        background-color: ${p => p.theme.color.app.major.normal};
        color: ${p => p.theme.color.app.minor.normal};
    }

    .lucide {
        height: ${p => p.theme.global.typography.lineHeight};
        width: ${p => p.theme.global.typography.lineHeight};
        stroke-width: 0.1em;
    }
`;

/**
 * ThemeProvider:
 * ---
 * styled-components has full theming support by exporting a <ThemeProvider> wrapper
 * component. This component provides a theme to all React components underneath itself
 * via the context API.
 * In the render tree all styled-components will have access to the provided theme, even
 * when they are multiple levels deep. To illustrate this, let's create our Button
 * component, but this time we'll pass some variables down as a theme.
 * [`styled-components documentation`](https://styled-components.com/docs/advanced#theming)
 * ---
 * createGlobalStyle:
 * ---
 * A helper function to generate a special StyledComponent that handles global styles.
 * Normally, styled components are automatically scoped to a local CSS class and therefore
 * isolated from other components. In the case of createGlobalStyle, this limitation is
 * removed and things like CSS resets or base stylesheets can be applied.
 * [`styled-components documentation`](https://styled-components.com/docs/api#helpers)
 */
export function ThemeProviderRegistry({ children }: R.PropsWithChildren) {
    const { theme } = R.useContext(ThemeContext);

    return (
        <ThemeProvider theme={Themes[theme]}>
            <GlobalStyle />
            {children}
        </ThemeProvider>
    );
}
