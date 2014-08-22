loadScript = (url, callback) ->
  head = document.getElementsByTagName("head")[0]
  script = document.createElement("script")
  script.type = "text/javascript"
  script.src = url
  script.onreadystatechange = callback
  script.onload = callback
  head.appendChild script
  return

pakopakoApp = ->
  pakopako = angular.module("pakopako", [])

  # {{ -> [[
  pakopako.config ($interpolateProvider) ->
    $interpolateProvider.startSymbol "[["
    $interpolateProvider.endSymbol "]]"
    return

  pakopako.controller "TodoController", [
    "$scope"
    ($scope) ->
      $scope.todos = [
        {
          text: "learn angular"
          done: true
        }
        {
          text: "build an angular app"
          done: false
        }
      ]
      $scope.addTodo = ->
        $scope.todos.push
          text: $scope.todoText
          done: false

        $scope.todoText = ""
        return

      $scope.remaining = ->
        count = 0
        angular.forEach $scope.todos, (todo) ->
          count += (if todo.done then 0 else 1)
          return

        count

      $scope.archive = ->
        oldTodos = $scope.todos
        $scope.todos = []
        angular.forEach oldTodos, (todo) ->
          $scope.todos.push todo  unless todo.done
          return

        return
  ]

url = document.URL + "static/js/bower_components/angular/angular.min.js"
loadScript url, pakopakoApp
