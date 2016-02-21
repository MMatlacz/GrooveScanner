angular.module 'upc'
  .factory 'Airport', (API, $resource) ->
    'ngInject'

    resource = $resource API + 'airports/', null

    return {
      cache: null
      query: (lng, lat) ->
        @cache = resource.query({lng: lng, lat: lat})
    }

