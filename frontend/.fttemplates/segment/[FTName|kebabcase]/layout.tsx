import type { Metadata } from 'next';
import { PropsWithChildren } from 'react';

export const metadata: Metadata = { title: '[FTName|sentencecase]' };

export default function [FTName|pascalcase]Layout({ children }: PropsWithChildren) {
    return <>{children}</>;
}
