import 'styled-components';

import { ITheme } from './theme/types/final.type';

// Register to receive suggestions in the IDE.
declare module 'styled-components' {
    export interface DefaultTheme extends ITheme {}
}
