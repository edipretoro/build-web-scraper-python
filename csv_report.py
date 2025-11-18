import csv


def write_csv_report(page_data, filename="report.csv"):
    fieldnames = [
        "page_url",
        "h1",
        "first_paragraph",
        "outgoing_link_urls",
        "image_urls",
    ]

    with open(filename, mode="w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for data in page_data:
            writer.writerow({
                "page_url": data["url"],
                "h1": data["h1"],
                "first_paragraph": data["first_paragraph"],
                "outgoing_link_urls": ";".join(data["outgoing_links"]),
                "image_urls": ";".join(data["image_urls"]),
            })