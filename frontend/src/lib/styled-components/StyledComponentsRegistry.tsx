'use client';

import { useServerInsertedHTML } from 'next/navigation';
import { PropsWithChildren, useState } from 'react';
import { ServerStyleSheet, StyleSheetManager } from 'styled-components';

/**
 * Use the styled-components API to create a global registry component to collect all CSS
 * style rules generated during a render, and a function to return those rules.
 * Then use the useServerInsertedHTML hook to inject the styles collected in the registry
 * into the <head> HTML tag in the root layout.
 * [`Next.js documentation`](https://nextjs.org/docs/app/building-your-application/styling/css-in-js#styled-components)
 */
export function StyledComponentsRegistry({ children }: PropsWithChildren) {
    const [styledComponentsStyleSheet] = useState(() => new ServerStyleSheet());

    useServerInsertedHTML(() => {
        const styles = styledComponentsStyleSheet.getStyleElement();
        styledComponentsStyleSheet.instance.clearTag();
        return <>{styles}</>;
    });

    if (typeof window !== 'undefined') return <>{children}</>;

    return (
        <StyleSheetManager sheet={styledComponentsStyleSheet.instance}>
            {children}
        </StyleSheetManager>
    );
}
