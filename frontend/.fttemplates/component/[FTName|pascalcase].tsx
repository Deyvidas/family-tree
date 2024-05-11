'use client';

import R from 'react';
import styled, { DefaultTheme } from 'styled-components';

const Tag: R.ElementType = 'div';
type DefaultProps = R.ComponentPropsWithoutRef<typeof Tag>;
type CompletedProps = Required<Omit<IProps, keyof DefaultProps>> & DefaultProps;

interface IProps extends DefaultProps {
    theme?: DefaultTheme;
}

export function [FTName|pascalcase](props: IProps) {
    return <Styled[FTName|pascalcase] {...props} />;
};

const Styled[FTName|pascalcase] = styled(Tag)<CompletedProps>``;