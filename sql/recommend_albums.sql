SELECT album.title
FROM track
JOIN album ON (track.album_id = album.album_id)
WHERE LOWER(track.name) = LOWER('Enter Sandman')