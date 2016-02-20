angular.module 'upc'
  .factory 'Airport', (API, $resource) ->
    'ngInject'

    resource = $resource API + 'airports/', null

    return {
      query: -> resource.query()
    }

