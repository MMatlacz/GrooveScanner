angular.module 'upc'
  .config ($logProvider, $resourceProvider) ->
    'ngInject'

    $resourceProvider.defaults.stripTrailingSlashes = false
    $logProvider.debugEnabled true
