angular.module 'upc'
  .factory 'Event', (API, $resource) ->
    'ngInject'

    resource = $resource API + 'event/:id/', {'id': '@id'},
      query:
        method: 'GET'
        isArray: true

      get:
        method: 'GET'

    return {
      query: (querystring) -> resource.query({q: querystring})
      get: (id) -> resource.get({id: id})
    }

