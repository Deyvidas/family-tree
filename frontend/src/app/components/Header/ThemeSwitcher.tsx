import { Moon, Sun } from 'lucide-react';
import R from 'react';

import { ThemeContext } from '@/lib/styled-components/ThemeContextProvider';

import { Button } from '@/components/Button';

export function ThemeSwitcher() {
    const { theme, setTheme } = R.useContext(ThemeContext);

    function switchTheme() {
        switch (theme) {
            case 'dark':
                return setTheme('light');

            case 'light':
                return setTheme('dark');

            default:
                throw Error(`Passed unexpected theme ${theme}`);
        }
    }

    return (
        <Button
            $color='primary'
            $variant='outlined'
            onClick={switchTheme}
        >
            {theme === 'light' && <Sun />}
            {theme === 'dark' && <Moon />}
        </Button>
    );
}
