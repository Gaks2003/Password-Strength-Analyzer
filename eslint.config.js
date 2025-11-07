module.exports = [
    {
        languageOptions: {
            ecmaVersion: 'latest',
            sourceType: 'script',
            globals: {
                document: 'readonly',
                window: 'readonly',
                console: 'readonly',
                alert: 'readonly',
                prompt: 'readonly',
                setTimeout: 'readonly',
                setInterval: 'readonly',
                URL: 'readonly',
                Blob: 'readonly',
                Math: 'readonly',
                Set: 'readonly',
                Object: 'readonly'
            }
        },
        rules: {
            'indent': ['error', 4],
            'quotes': ['error', 'single'],
            'semi': ['error', 'always'],
            'no-unused-vars': 'warn',
            'no-console': 'off',
            'prefer-const': 'error',
            'no-var': 'error',
            'eqeqeq': 'error',
            'curly': 'error',
            'no-trailing-spaces': 'error',
            'eol-last': 'error',
            'no-useless-escape': 'error'
        }
    }
];