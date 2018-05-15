const CopyWebpackPlugin = require('copy-webpack-plugin');

const assetPath = `${__dirname}/emoji_picker/static/emoji_picker`;

module.exports = {
    mode: 'production',
    devtool: 'source-map',
    output: {
        path: assetPath,
        publicPath: assetPath,
        filename: 'emoji-picker.js',
    },
    plugins: [
        new CopyWebpackPlugin([
            { from: 'node_modules/emoji-mart/css/emoji-mart.css', to: `${assetPath}/emoji-picker-panel.css` },
            { from: 'src/style.css', to: `${assetPath}/emoji-picker-main.css` },
        ], {}),
    ],
};
