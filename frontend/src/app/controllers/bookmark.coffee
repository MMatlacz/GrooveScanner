angular.module 'upc'
  .controller 'BookmarkController', ($scope, $rootScope, $sce, $stateParams, toastr, Airport, Event) ->
    'ngInject'

    $rootScope.bgstate = 'high'

    $scope.event = null
    $scope.loading_failed = null

    Event.get($stateParams.event_id).$promise.then (event) ->
      $scope.event = event
      url = "https:\/\/www.google.com/maps/embed?pb=!1m14!1m12!1m3!1d11972.733584287987!2d" + \
        event.venue.longitude + "!3d" + event.venue.latitude + \
        "!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!5e0!3m2!1spl!2ses!4v1456007953889"
      $scope.event_map = $sce.trustAsResourceUrl url
    , ->
      $scope.loading_failed = 'Error loading event details. Please try again.'

    @