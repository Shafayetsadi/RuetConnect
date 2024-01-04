/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
    content: [
        /**
         * HTML. Paths to Django template files that will contain Tailwind CSS classes.
         */

        /*  Templates within theme app (<tailwind_app_name>/templates), e.g. base.html. */
        '../templates/**/*.html',
        '../../campus/static/campus/css/*.css',

        /*
         * Main templates directory of the project (BASE_DIR/templates).
         * Adjust the following line to match your project structure.
         */
        '../../templates/**/*.html',

        /*
         * Templates in other django apps (BASE_DIR/<any_app_name>/templates).
         * Adjust the following line to match your project structure.
         */
        '../../**/templates/**/*.html',

        /**
         * JS: If you use Tailwind CSS in JavaScript, uncomment the following lines and make sure
         * patterns match your project structure.
         */
        /* JS 1: Ignore any JavaScript in node_modules folder. */
        // '!../../**/node_modules',
        /* JS 2: Process all JavaScript files in the project. */
        // '../../**/*.js',

        /**
         * Python: If you use Tailwind CSS classes in Python, uncomment the following line
         * and make sure the pattern below matches your project structure.
         */
        '../../**/*.py'
    ],
    theme: {
        extend: {
            colors: {
                'background': 'var(--background)',
                'foreground': 'var(--foreground)',
                'card': 'var(--card)',
                'card-foreground': 'var(--card-foreground)',
                'popover': 'var(--popover)',
                'popover-foreground': 'var(--popover-foreground)',
                'primary': 'var(--primary)',
                'primary-foreground': 'var(--primary-foreground)',
                'secondary': 'var(--secondary)',
                'secondary-foreground': 'var(--secondary-foreground)',
                'muted': 'var(--muted)',
                'muted-foreground': 'var(--muted-foreground)',
                'accent': 'var(--accent)',
                'accent-foreground': 'var(--accent-foreground)',
                'destructive': 'var(--destructive)',
                'destructive-foreground': 'var(--destructive-foreground)',
                'border': 'var(--border)',
                'input': 'var(--input)',
                'ring': 'var(--ring)',
                'radius': '0.5rem',
            },
            
        },
    },
    plugins: [
        /**
         * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
         * for forms. If you don't like it or have own styling for forms,
         * comment the line below to disable '@tailwindcss/forms'.
         */
        // require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/line-clamp'),
        require('@tailwindcss/aspect-ratio'),
        'prettier-plugin-tailwindcss',
    ],
}
