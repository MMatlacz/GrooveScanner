angular.module 'upc'
  .factory 'Wolfram', (API, $resource) ->
    'ngInject'

    resource = $resource API + 'wolfram/:id/', {'id': '@id'}

    return {
      get: (code) ->
        return resource.get({id: code})
    }

