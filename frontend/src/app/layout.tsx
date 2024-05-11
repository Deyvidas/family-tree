import type { Metadata } from 'next';
import R from 'react';

import { StyledComponentsRegistry } from '@/lib/styled-components/StyledComponentsRegistry';
import { ThemeContextProvider } from '@/lib/styled-components/ThemeContextProvider';
import { ThemeProviderRegistry } from '@/lib/styled-components/ThemeProviderRegistry';

import './globals.css';

import { Container } from './components/Container';
import { Content } from './components/Content';
import { Footer } from './components/Footer';
import { Header } from './components/Header/Header';
import { ScrollTop } from './components/ScrollTop';

export const metadata: Metadata = {
    title: 'Family tree app',
};

export default function RootLayout({ children }: R.PropsWithChildren) {
    return (
        <html lang='ru'>
            <body>
                <StyledComponentsRegistry>
                    <ThemeContextProvider>
                        <ThemeProviderRegistry>
                            <Container>
                                <Header />
                                <Content>{children}</Content>
                                <Footer />
                                <ScrollTop />
                            </Container>
                        </ThemeProviderRegistry>
                    </ThemeContextProvider>
                </StyledComponentsRegistry>
            </body>
        </html>
    );
}
