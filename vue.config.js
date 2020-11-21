const path = require("path");
const CompressionWebpackPlugin = require('compression-webpack-plugin');
// const productionGzipExtensions = /\.(js|css|json|txt|html|ico|svg)(\?.*)?$/i;
const BundleAnalyzerPlugin = require("webpack-bundle-analyzer").BundleAnalyzerPlugin;
const isProduction = process.env.NODE_ENV !== 'development';
const devNeedCdn = false;
const cdn = {
  // cdn：模块名称和模块作用域命名（对应window里面挂载的变量名称）
  externals: {
      vue: 'Vue',
      vuex: 'Vuex',
      'vue-router': 'VueRouter',
      'axios': 'axios',
      'ElementUI': 'element-ui',
    'ECharts': 'echarts',
  },
  // cdn的css链接
  css: [
  ],
  // cdn的js链接
  js: [
      'https://cdn.bootcss.com/vue/2.6.10/vue.min.js',
      'https://cdn.bootcss.com/vuex/3.1.2/vuex.min.js',
      'https://cdn.bootcss.com/vue-router/3.1.3/vue-router.min.js',
      'https://cdn.bootcss.com/axios/0.19.2/axios.min.js'
  ]
}
module.exports = {
  
  // 基本路径  baseUrl 自cli3.3起以弃用
  publicPath: process.env.NODE_ENV === "production" ? "" : "/",
  // 输出文件目录
  outputDir: process.env.NODE_ENV === "production" ? "dist" : "devdist",
  // eslint-loader 是否在保存的时候检查
  lintOnSave: false,
  // webpack配置
  // see https://github.com/vuejs/vue-cli/blob/dev/docs/webpack.md
  chainWebpack: (config) => {
    config
      .plugin('webpack-bundle-analyzer')
      .use(BundleAnalyzerPlugin)
      config.plugin('html').tap(args => {
        // 生产环境或本地需要cdn时，才注入cdn
        if (isProduction || devNeedCdn) args[0].cdn = cdn
        return args
    })
  },
  configureWebpack: config => {
    if (isProduction || devNeedCdn) config.externals = cdn.externals
    config.resolve = {
      extensions: [".js", ".json", ".vue"],
      alias: {
        "vue$": "vue/dist/vue.js",
        "@": path.resolve(__dirname, "./src"),
        "@c": path.resolve(__dirname, "./src/components"),
        "@api": path.resolve(__dirname, "./src/api"),
        "@static": path.resolve(__dirname, "./src/static"),
      },
    },
    config.plugins.push(
      new CompressionWebpackPlugin(
        {
          filename: info => {
            return `${info.path}.gz${info.query}`
          },
          algorithm: 'gzip',
          threshold: 10240, // 只有大小大于该值的资源会被处理 10240
          test: new RegExp('\\.(' + ['js'].join('|') + ')$'
          ),
          minRatio: 0.8, // 只有压缩率小于这个值的资源才会被处理
          deleteOriginalAssets: false // 删除原文件
        }
      )
    );
  },
  // vue-loader 配置项
  // https://vue-loader.vuejs.org/en/options.html
  // vueLoader: {},
  // 生产环境是否生成 sourceMap 文件
  productionSourceMap: false,
  // css相关配置
  css: {
    // 是否使用css分离插件 ExtractTextPlugin
    extract: true,
    // 开启 CSS source maps?
    sourceMap: false,
    requireModuleExtension: true,
    // css预设器配置项
    loaderOptions: {
      sass: {
        // prependData: `@import "./src/style/main.scss";`,
        additionalData: `@import "./src/style/main.scss";`
      },
    },
  },

    
  // use thread-loader for babel & TS in production build
  // enabled by default if the machine has more than 1 cores
  parallel: require("os").cpus().length > 1,
  // 是否启用dll
  // See https://github.com/vuejs/vue-cli/blob/dev/docs/cli-service.md#dll-mode
  // dll: false,
  // PWA 插件相关配置
  // see vuejs/vue-cli
  pwa: {},
  // webpack-dev-server 相关配置
  devServer: {
    proxy: {
      '/api': {
        target: 'http://10.26.27.45:80',
        ws: true,
        changeOrigin: true
      }
    }
  },
  // 第三方插件配置
  pluginOptions: {
    // ...
  },
  transpileDependencies: [
    'resize-detector'
  ]
};
