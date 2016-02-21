angular.module 'upc'
  .controller 'HomeController', ($scope, $rootScope, $timeout, $state, $geolocation, toastr, Airport, Event) ->
    'ngInject'

    $rootScope.bgstate = 'low'

    $geolocation.getCurrentPosition({timeout: 18000}).then (position) ->
      if not $scope.search.airport
        minimal_distance = null
        found_airport = null

        for airport in $scope.search.airports
          distance = Math.sqrt(
            Math.pow(position.coords.latitude - airport.lat, 2) +
            Math.pow(position.coords.longitude - airport.lng, 2)
          )

          if minimal_distance == null or  distance < minimal_distance
            minimal_distance = distance
            found_airport = airport

        $scope.search.airport = found_airport


    $scope.search =
      typeahead: []
      airports: Airport.query()

      event:null
      airport: null

      loading: false
      search: (query) ->
        return Event.query(query).$promise.then (data) ->
          return data

      submit: ->
        console.log $scope.search

        if not $scope.search.airport or not $scope.search.event
          toastr.error 'You must input starting airport and event you want to go on.'
          return

        $state.go 'bookmark', {'event_id': $scope.search.event.id, 'airport': $scope.search.airport.code}
    @
