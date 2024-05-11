'use client';

import { ArrowUpToLine } from 'lucide-react';
import R from 'react';
import styled, { DefaultTheme } from 'styled-components';

import { Button } from '@/components/Button';

type DefaultProps = Omit<R.ComponentPropsWithoutRef<typeof Button>, 'children'>;
type CompletedProps = Required<Omit<IProps, keyof DefaultProps>> & DefaultProps;

interface IProps extends DefaultProps {
    theme?: DefaultTheme;
}

export function ScrollTop(props: IProps) {
    return (
        <StyledScrollTop
            {...props}
            onClick={() => window.scroll(0, 0)}
        >
            <ArrowUpToLine />
        </StyledScrollTop>
    );
}

const StyledScrollTop = styled(Button)<CompletedProps>`
    position: fixed;
    right: 2rem;
    bottom: 2rem;
`;
