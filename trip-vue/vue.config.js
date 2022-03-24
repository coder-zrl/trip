module.exports = {
  publicPath: './',
    outputDir: 'dist',
    assetsDir:'static',
  configureWebpack: {
    resolve: {
      alias: {
        'assets':'@/assets',
        'common':'@/common',
        'components':'@/components',
        'network':'@/network',
        'views':'@/views'
      }
    }
  }
}