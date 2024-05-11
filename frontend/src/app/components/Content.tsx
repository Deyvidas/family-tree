'use client';

import R from 'react';
import styled, { DefaultTheme, css } from 'styled-components';

const Tag: R.ElementType = 'main';
type DefaultProps = R.ComponentPropsWithoutRef<typeof Tag>;
type CompletedProps = Required<Omit<IProps, keyof DefaultProps>> & DefaultProps;

interface IProps extends DefaultProps {
    theme?: DefaultTheme;
}

export function Content(props: IProps) {
    return <StyledContent {...props} />;
}

const StyledContent = styled(Tag)<CompletedProps>`
    flex-grow: 1;
    padding-block: 1em;
    ${p => getPaddingInline(p)}

    display: flex;
    flex-direction: column;
    align-items: center;
    row-gap: 0.5em;

    color: ${p => p.theme.color.primary.major.normal};
`;

function getPaddingInline(props: CompletedProps) {
    const { minPadding, minWidth } = props.theme.global.container;

    return css`
        padding-inline: max(calc((100% - ${minWidth}) / 2), ${minPadding});
    `;
}
