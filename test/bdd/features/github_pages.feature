Feature: GitHub Pages landing page
  As a maintainer
  I want a basic click-through check and screenshot
  So the published site is validated visually

  Scenario: Capture a landing page screenshot and click a link
    Given the GitHub Pages site is reachable
    When I capture a screenshot of the landing page
    And I click the first available link
    Then the page should include the text "VLC"
