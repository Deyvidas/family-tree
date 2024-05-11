import { CSSProperties } from 'styled-components';

export interface ISharedThemeAttributes {
    global: {
        container: {
            minWidth: CSSProperties['width'];
            minPadding: CSSProperties['paddingInline' | 'paddingLeft' | 'paddingRight'];
        };

        typography: {
            fontSize: CSSProperties['fontSize'];
            fontWeight: keyof ISharedThemeAttributes['global']['fontWeights'];
            lineHeight: CSSProperties['lineHeight'];
            fontFamily: CSSProperties['fontFamily'];
        };

        fontWeights: {
            light: CSSProperties['fontWeight'];
            regular: CSSProperties['fontWeight'];
            medium: CSSProperties['fontWeight'];
            bold: CSSProperties['fontWeight'];
        };
    };

    typography: {
        h1: ITypographyParameters;
        h2: ITypographyParameters;
        h3: ITypographyParameters;
        h4: ITypographyParameters;
        h5: ITypographyParameters;
        h6: ITypographyParameters;
        textXL: ITypographyParameters;
        textL: ITypographyParameters;
        textNormal: ITypographyParameters;
        textS: ITypographyParameters;
        textXS: ITypographyParameters;
    };

    padding: {
        xs: CSSProperties['padding'];
        s: CSSProperties['padding'];
        normal: CSSProperties['padding'];
        l: CSSProperties['padding'];
        xl: CSSProperties['padding'];
    };

    borderRadius: {
        square: CSSProperties['borderRadius'];
        xs: CSSProperties['borderRadius'];
        s: CSSProperties['borderRadius'];
        normal: CSSProperties['borderRadius'];
        l: CSSProperties['borderRadius'];
        xl: CSSProperties['borderRadius'];
        circle: CSSProperties['borderRadius'];
    };

    transition: {
        onHover: ITransitionParameters;
    };
}

interface ITypographyParameters {
    fontFamily: CSSProperties['fontFamily'];
    fontWeight: keyof ISharedThemeAttributes['global']['fontWeights'];
    fontSize: CSSProperties['fontSize'];
    lineHeight: CSSProperties['lineHeight'];
}

interface ITransitionParameters {
    duration: CSSProperties['transitionDuration'];
    function: CSSProperties['transitionTimingFunction'];
}
