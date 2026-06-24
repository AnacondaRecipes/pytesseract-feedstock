"""Correctness test for pytesseract.

Same test as the tesseract feedstock, expressed through pytesseract's Python API:
OCR eurotext.tif with the multi-language flag and compare the result byte-for-byte
against the captured baseline (eurotext.expected.txt, copied from tesseract-feedstock).

A "did it crash" smoke test passes even when OCR returns an empty string -- which is
exactly what a missing tesseract binary or tessdata produces, the real risk on a
newly-enabled platform (win-64, PKG-13803). Comparing to a known baseline catches that.

Tesseract is deterministic for a given binary + tessdata + flags. If a future bump
trips this and the OCR genuinely got better, regenerate eurotext.expected.txt and note
it in the PR.
"""
from PIL import Image
import pytesseract

with open("eurotext.expected.txt", encoding="utf-8") as f:
    expected = f.read()

actual = pytesseract.image_to_string(
    Image.open("eurotext.tif"),
    lang="eng+deu+fra+ita+spa+por",
)

assert actual == expected, (
    f"OCR output did not match baseline.\n"
    f"--- expected ---\n{expected!r}\n"
    f"--- actual ---\n{actual!r}"
)
print("OCR output matches baseline.")
