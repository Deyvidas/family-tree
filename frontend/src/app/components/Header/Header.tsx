'use client';

import { Blocks } from 'lucide-react';
import R from 'react';
import styled, { DefaultTheme, RuleSet, css } from 'styled-components';

import { Link } from '@/components/Link';

import { NavLinks } from './NavLinks';
import { ThemeSwitcher } from './ThemeSwitcher';

const Tag: R.ElementType = 'header';
type DefaultProps = Omit<R.ComponentPropsWithoutRef<typeof Tag>, 'children'>;
type CompletedProps = Required<Omit<IProps, keyof DefaultProps>> & DefaultProps;

interface IProps extends DefaultProps {
    theme?: DefaultTheme;
}

export function Header(props: IProps) {
    return (
        <StyledHeader {...props}>
            <Link href='/'>
                <Blocks />
            </Link>
            <NavLinks />
            <ThemeSwitcher />
        </StyledHeader>
    );
}

const StyledHeader = styled(Tag)<CompletedProps>`
    position: sticky;
    top: 0;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding-block: 1em;
    ${p => getPaddingInline(p)}

    backdrop-filter: blur(3px);
    border-bottom: 0.1em solid ${p => p.theme.color.primary.major.normal};
`;

function getPaddingInline(props: CompletedProps): RuleSet {
    const { minPadding, minWidth } = props.theme.global.container;

    return css`
        padding-inline: max(calc((100% - ${minWidth}) / 2), ${minPadding});
    `;
}
