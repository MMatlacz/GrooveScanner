angular.module 'upc'
  .factory 'Airport', (API, $resource) ->
    'ngInject'

    resource = $resource API + 'airports/:id/', {'id': '@id'}

    return {
      cache: null
      query: (lng, lat) ->
        @cache = resource.query({lng: lng, lat: lat})
        return @cache
      get: (code) ->
        return resource.get({id: code})
    }

