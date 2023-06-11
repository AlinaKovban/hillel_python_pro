from flask import Flask
from webargs import fields
from webargs.flaskparser import use_kwargs


from database_handler import execute_query

app = Flask(__name__)


def format_records(records):
    return "<br>".join(str(record) for record in records)


@app.route("/order-price")
@use_kwargs(
    {
         "country": fields.Str(
          missing=None
         ),
    },
    location="query"
)
def order_price(country):
    query = """SELECT UnitPrice * Quantity AS Sales, BillingCountry
               FROM invoice_items
               LEFT JOIN invoices ON
               invoice_items.InvoiceId = invoices.InvoiceId
            """

    fields = {}

    if country:
        fields["BillingCountry"] = country

    if fields:
        query += " WHERE " + " AND ".join(
            f"{key}='{value}'" for key, value in fields.items()
         )
    records = execute_query(query=query)
    return format_records(records)


@app.route("/all_tracks")
@use_kwargs(
    {
         "track_id": fields.Str(
          missing=None
         ),
    },
    location="query"
)
def get_all_info_about_track(track_id):
    query = """SELECT tracks.*,
                      albums.*,
                      artists.*,
                      media_types.*,
                      genres.*,
                      invoice_items.InvoiceLineId,
                      invoice_items.InvoiceId,
                      invoice_items.TrackId AS invoice_items_TrackId,
                      invoice_items.UnitPrice,
                      invoice_items.Quantity,
                      invoices.*,
                      customers.*,
                      employees.*,
                      playlist_track.PlaylistId,
                      playlist_track.TrackId AS playlist_track_TrackId,
                      playlists.*
               FROM tracks
               JOIN albums ON tracks.AlbumId = albums.AlbumId
               JOIN artists ON albums.ArtistId  = artists.ArtistId
               JOIN media_types ON tracks.MediaTypeId = media_types.MediaTypeId
               JOIN genres ON tracks.GenreId = genres.GenreId
               JOIN invoice_items ON tracks.TrackId = invoice_items.TrackId
               JOIN invoices ON invoices.InvoiceId = invoice_items.InvoiceId
               JOIN customers ON invoices.CustomerId = customers.CustomerId
               JOIN employees ON employees.EmployeeId = customers.SupportRepId
               JOIN playlist_track ON tracks.TrackId = playlist_track.TrackId
               JOIN playlists ON playlists.PlaylistId = playlist_track.PlaylistId
            """

    if track_id:
        query += f" WHERE tracks.TrackId = '{track_id}'"

    query += " GROUP BY tracks.TrackId"

    records = execute_query(query=query)
    return format_records(records)


@app.route("/hours_of_all_tracks")
def hours_of_all_tracks():
    query = """SELECT SUM(Milliseconds) / 3600000 AS hours_of_all_tracks
               FROM tracks
            """

    records = execute_query(query=query)
    return f"Here is the quantity of hours of all tracks {records[0][0]}"
