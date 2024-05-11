'use client';

import R from 'react';
import styled, { DefaultTheme } from 'styled-components';

import { Link } from '@/components/Link';

const Tag: R.ElementType = 'div';
type DefaultProps = R.ComponentPropsWithoutRef<typeof Tag>;
type CompletedProps = Required<Omit<IProps, keyof DefaultProps>> & DefaultProps;

interface IProps extends DefaultProps {
    theme?: DefaultTheme;
}

export function NavLinks(props: IProps) {
    return (
        <StyledNavLinks {...props}>
            <Link
                href='/person/all'
                $color='secondary'
            >
                all persons
            </Link>
        </StyledNavLinks>
    );
}

const StyledNavLinks = styled(Tag)<CompletedProps>`
    display: flex;
    column-gap: ${p => p.theme.padding.normal};
`;
