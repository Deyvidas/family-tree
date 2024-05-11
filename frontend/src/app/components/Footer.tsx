'use client';

import R from 'react';
import styled, { DefaultTheme, RuleSet, css } from 'styled-components';

const Tag: R.ElementType = 'div';
type DefaultProps = Omit<R.ComponentPropsWithoutRef<typeof Tag>, 'children'>;
type CompletedProps = Required<Omit<IProps, keyof DefaultProps>> & DefaultProps;

interface IProps extends DefaultProps {
    theme?: DefaultTheme;
}

export function Footer(props: IProps) {
    return <StyledFooter {...props}>Footer</StyledFooter>;
}

const StyledFooter = styled(Tag)<CompletedProps>`
    display: flex;
    align-items: center;
    padding-block: 1em;
    ${p => getPaddingInline(p)}

    color: ${p => p.theme.color.primary.major.normal};
    border-top: 0.1em solid ${p => p.theme.color.primary.major.normal};
`;

function getPaddingInline(props: CompletedProps): RuleSet {
    const { minPadding, minWidth } = props.theme.global.container;

    return css`
        padding-inline: max(calc((100% - ${minWidth}) / 2), ${minPadding});
    `;
}
