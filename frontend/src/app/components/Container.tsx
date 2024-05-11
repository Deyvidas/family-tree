'use client';

import R from 'react';
import styled, { DefaultTheme } from 'styled-components';

const Tag: R.ElementType = 'div';
type DefaultProps = R.ComponentPropsWithoutRef<typeof Tag>;
type CompletedProps = Required<Omit<IProps, keyof DefaultProps>> & DefaultProps;

interface IProps extends DefaultProps {
    theme?: DefaultTheme;
}

export function Container(props: IProps) {
    return <StyledContainer {...props} />;
}

const StyledContainer = styled(Tag)<CompletedProps>`
    min-height: 100%;
    display: flex;
    flex-direction: column;
    font-size: 1.6em;
`;
