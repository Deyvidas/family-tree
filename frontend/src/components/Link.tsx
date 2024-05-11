'use client';

import NextLink from 'next/link';
import { usePathname } from 'next/navigation';
import R from 'react';
import styled, { DefaultTheme, RuleSet, css } from 'styled-components';

import { IColorCategories } from '@/lib/styled-components/theme/types/color.type';

const Tag: R.ElementType = 'a';
type DefaultProps = R.ComponentPropsWithoutRef<typeof Tag>;
type CompletedProps = Required<Omit<IProps, keyof DefaultProps>> & DefaultProps;

interface IProps extends DefaultProps {
    theme?: DefaultTheme;
    href: string;
    $color?: keyof IColorCategories;
    $isActive?: boolean;
}

export function Link(props: IProps) {
    const pathname = usePathname();
    const { href, ...rest } = props;

    return (
        <NextLink
            href={href}
            legacyBehavior
        >
            <StyledLink
                $color='primary'
                $isActive={pathname === href}
                {...rest}
            />
        </NextLink>
    );
}

const StyledLink = styled(Tag)<CompletedProps>`
    display: flex;
    align-items: center;
    column-gap: 0.3em;

    transition-property: color;
    transition-duration: ${p => p.theme.transition.onHover.duration};
    transition-timing-function: ${p => p.theme.transition.onHover.function};

    ${p => setColor(p)}
    cursor: pointer;
`;

function setColor(props: CompletedProps): RuleSet {
    const color = props.theme.color[props.$color];

    if (props.$isActive) {
        return css`
            text-decoration: underline !important;
            color: ${p => color.major.hover};
        `;
    } else {
        return css`
            color: ${p => color.major.normal};
            &:hover {
                color: ${p => color.major.hover};
            }
        `;
    }
}
