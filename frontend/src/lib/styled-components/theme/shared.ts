import { Rubik } from 'next/font/google';
import { CSSProperties } from 'styled-components';

import { ISharedThemeAttributes } from './types/shared.type';

const rubik = Rubik({ subsets: ['cyrillic'], weight: ['400', '500', '600', '700'] });
const fontFamily: CSSProperties['fontFamily'] = rubik.style.fontFamily;
const lineHeight: CSSProperties['lineHeight'] = '1.4em';

export const ThemeSharedValues: ISharedThemeAttributes = {
    global: {
        container: {
            minWidth: '1150px',
            minPadding: '30px',
        },

        typography: {
            fontFamily: fontFamily,
            fontSize: '10px',
            lineHeight: lineHeight,
            fontWeight: 'regular',
        },

        fontWeights: {
            light: 400,
            regular: 500,
            medium: 600,
            bold: 700,
        },
    },

    typography: {
        h1: {
            fontFamily: fontFamily,
            fontSize: '3rem',
            lineHeight: lineHeight,
            fontWeight: 'bold',
        },

        h2: {
            fontFamily: fontFamily,
            fontSize: '2.8rem',
            lineHeight: lineHeight,
            fontWeight: 'bold',
        },

        h3: {
            fontFamily: fontFamily,
            fontSize: '2.6rem',
            lineHeight: lineHeight,
            fontWeight: 'bold',
        },

        h4: {
            fontFamily: fontFamily,
            fontSize: '2.3rem',
            lineHeight: lineHeight,
            fontWeight: 'medium',
        },

        h5: {
            fontFamily: fontFamily,
            fontSize: '2rem',
            lineHeight: lineHeight,
            fontWeight: 'medium',
        },

        h6: {
            fontFamily: fontFamily,
            fontSize: '1.8rem',
            lineHeight: lineHeight,
            fontWeight: 'medium',
        },

        textXL: {
            fontFamily: fontFamily,
            fontSize: '2rem',
            lineHeight: lineHeight,
            fontWeight: 'regular',
        },

        textL: {
            fontFamily: fontFamily,
            fontSize: '1.8rem',
            lineHeight: lineHeight,
            fontWeight: 'regular',
        },

        textNormal: {
            fontFamily: fontFamily,
            fontSize: '1.6rem',
            lineHeight: lineHeight,
            fontWeight: 'regular',
        },

        textS: {
            fontFamily: fontFamily,
            fontSize: '1.3rem',
            lineHeight: lineHeight,
            fontWeight: 'light',
        },

        textXS: {
            fontFamily: fontFamily,
            fontSize: '1rem',
            lineHeight: lineHeight,
            fontWeight: 'light',
        },
    },

    padding: {
        xs: '0.1em',
        s: '0.3em',
        normal: '0.5em',
        l: '0.7em',
        xl: '0.9em',
    },

    borderRadius: {
        square: '0.3em',
        xs: '0.5em',
        s: '1em',
        normal: '1.5em',
        l: '2em',
        xl: '2.5em',
        circle: '50%',
    },

    transition: {
        onHover: {
            duration: '0.3s',
            function: 'ease-in',
        },
    },
};
