<!--
     <INVISOMARK - Greatest Watermark Software>
        Copyright (C) <2023>  <YuexuChen>

        This program is free software: you can redistribute it and/or modify
        it under the terms of the GNU General Public License as published by
        the Free Software Foundation, either version 3 of the License, or
        (at your option) any later version.

        This program is distributed in the hope that it will be useful,
        but WITHOUT ANY WARRANTY; without even the implied warranty of
        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
        GNU General Public License for more details.

        You should have received a copy of the GNU General Public License
        along with this program.  If not, see <https://www.gnu.org/licenses/>.

 -->

<?php

function fetch_google_lens_page_token($api_key, $image_url, $language = null, $country = null, $no_cache = null, $async_param = null) {
    $base_url = "https://serpapi.com/search";
    $params = [
        "engine" => "google_lens",
        "api_key" => $api_key,
        "url" => $image_url,
        "hl" => $language,
        "country" => $country,
        "no_cache" => $no_cache,
        "async" => $async_param
    ];

    $params = array_filter($params, function($value) { return !is_null($value); });
    $query_string = http_build_query($params);
    $ch = curl_init("$base_url?$query_string");
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    $response = curl_exec($ch);
    curl_close($ch);

    $search_results = json_decode($response, true);
    return $search_results["image_sources_search"]["page_token"] ?? null;
}

function fetch_google_lens_image_sources($api_key, $page_token) {
    $base_url = "https://serpapi.com/search";
    $params = [
        "engine" => "google_lens_image_sources",
        "api_key" => $api_key,
        "page_token" => $page_token
    ];

    $query_string = http_build_query($params);
    $ch = curl_init("$base_url?$query_string");
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    $response = curl_exec($ch);
    curl_close($ch);

    return json_decode($response, true);
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $api_key = $_POST["api_key"];
    $image_url = $_POST["image_url"];

    $page_token = fetch_google_lens_page_token($api_key, $image_url);
    $image_sources_results = fetch_google_lens_image_sources($api_key, $page_token);

    echo "<pre>";
    print_r($image_sources_results);
    echo "</pre>";
}
?>
