'use client';

import R from 'react';
import styled, { DefaultTheme, RuleSet, css } from 'styled-components';

import { IColorCategories } from '@/lib/styled-components/theme/types/color.type';
import { ISharedThemeAttributes } from '@/lib/styled-components/theme/types/shared.type';

const Tag: R.ElementType = 'button';
type DefaultProps = R.ComponentPropsWithoutRef<typeof Tag>;
type CompletedProps = Required<Omit<IProps, keyof DefaultProps>> & DefaultProps;

interface IProps extends DefaultProps {
    theme?: DefaultTheme;
    $color?: keyof IColorCategories;
    $shape?: keyof ISharedThemeAttributes['borderRadius'];
    $variant?: 'contained' | 'outlined' | 'text';
}

export function Button(props: IProps) {
    return (
        <StyledButton
            $color='primary'
            $shape='square'
            $variant='contained'
            {...props}
        />
    );
}

export const StyledButton = styled(Tag)<CompletedProps>`
    display: flex;
    padding: ${p => p.theme.padding.s};
    align-items: center;
    justify-content: center;
    column-gap: ${p => p.theme.padding.s};

    ${p => getColors(p)}
    ${p => getBorderRadius(p)}
    ${p => getTransition(p)}
`;

function getColors(props: CompletedProps): RuleSet {
    const color = props.theme.color[props.$color];

    switch (props.$variant) {
        case 'contained':
            return css`
                color: ${color.minor.normal};
                background-color: ${color.major.normal};
                border-color: ${color.minor.normal};

                &:hover {
                    color: ${color.minor.hover};
                    background-color: ${color.major.hover};
                    border-color: ${color.minor.hover};
                }
            `;

        case 'outlined':
            return css`
                color: ${color.major.normal};
                border-color: ${color.major.normal};

                &:hover {
                    color: ${color.minor.hover};
                    background-color: ${color.major.hover};
                    border-color: ${color.minor.hover};
                }
            `;

        case 'text':
            return css`
                color: ${color.major.normal};

                &:hover {
                    color: ${color.minor.hover};
                    background-color: ${color.major.hover};
                }
            `;
    }
}

function getBorderRadius(props: CompletedProps): RuleSet {
    const { $shape, $variant } = props;

    const borderRadius = css`
        border-radius: ${p => p.theme.borderRadius[$shape ?? 'square']};
    `;

    if ($variant === 'text') {
        return borderRadius;
    }

    return css`
        border-width: 0.1em;
        border-style: solid;
        ${borderRadius}
    `;
}

function getTransition(props: CompletedProps): RuleSet {
    const staticValues = css`
        transition-duration: ${p => p.theme.transition.onHover.duration};
        transition-timing-function: ${p => p.theme.transition.onHover.function};
    `;

    switch (props.$variant) {
        case 'text':
            return css`
                ${staticValues};
                transition-property: color, background-color;
            `;

        default:
            return css`
                ${staticValues};
                transition-property: color, border-color, background-color;
            `;
    }
}
