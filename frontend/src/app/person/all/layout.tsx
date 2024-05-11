import type { Metadata } from 'next';
import { PropsWithChildren } from 'react';

export const metadata: Metadata = { title: 'All persons' };

export default function AllLayout({ children }: PropsWithChildren) {
    return <>{children}</>;
}
