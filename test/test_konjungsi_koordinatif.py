import unittest
from cfg_initialization import cfg_true_or_false


class TestKonjKoor(unittest.TestCase):
    def test_konj_koor_tak_hingga_01(self):
        """
        -> S-P-O (N-V-[N-KJ_KOOR-FN])
        (Polisi, nomina), (menemukan, verba), (pisau, nomina),
        (dan, konj_koor_tak_hingga), (senjata, nomina), (api, nomina),
        (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<verba>",
            "<nomina>",
            "<kj_koor_tak_hingga>",
            "<nomina>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_konj_koor_tak_hingga_02(self):
        """
        -> S-P-O (N-V-[N-KOMA-N-KOMA-KJ_KOOR-FN])
        (Polisi, nomina), (menemukan, verba), (ganja, nomina),
        (,, td_koma), (pisau, nomina), (,, td_koma),
        (dan, konj_koor_tak_hingga), (senjata, nomina),
        (api, nomina), (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<verba>",
            "<nomina>",
            "<td_koma>",
            "<nomina>",
            "<td_koma>",
            "<kj_koor_tak_hingga>",
            "<nomina>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_konj_koor_tak_hingga_03(self):
        """
        -> S-P ([N-N-KJ_KOOR-N]-[BUKAN-N-ADJ-ADV])
        (Telepon, nomina), (seluler, nomina), (,, td_koma), (komputer, nomina),
        (,, td_koma), (atau, konj_koor_tak_hingga), (internet, nomina), (bukan, bukan),
        (barang, nomina), (asing, adjektiva), (lagi, adverbia), (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<nomina>",
            "<td_koma>",
            "<nomina>",
            "<td_koma>",
            "<kj_koor_tak_hingga>",
            "<nomina>",
            "<bukan>",
            "<nomina>",
            "<adjektiva>",
            "<adverbia>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_konj_koor_terhingga_01(self):
        """
        -> S-P-PEL--KJ_KOOR-S-P (N-V-FPREP--KJ_KOOR-FN-FV)
        (Polisi, nomina), (tiba, verba), (di, preposisi), (lokasi, nomina),
        (,, td_koma), (tetapi, konj_koor_terhingga), (pencuri, nomina),
        (tersebut, verba), (sudah, adverbia), (pergi, verba),
        (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<verba>",
            "<preposisi>",
            "<nomina>",
            "<td_koma>",
            "<kj_koor_terhingga>",
            "<nomina>",
            "<verba>",
            "<adverbia>",
            "<verba>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_konj_koor_terhingga_klausa_01(self):
        """
        -> Kj Koor Terhingga Klausa 01
        (Anak, nomina), (kecil, adjektiva), (pun, pun), (sudah, adverbia),
        (mengerti, verba), (,, td_koma), (apalagi, kj_koor_terhingga_klausa),
        (orang, nomina), (dewasa, adjektiva), (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<adjektiva>",
            "<pun>",
            "<adverbia>",
            "<verba>",
            "<td_koma>",
            "<kj_koor_terhingga_klausa>",
            "<nomina>",
            "<adjektiva>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_konj_koor_klausa_01(self):
        """
        -> S-P-O--KOMA-P-PEL-F_KJ_SUB--KOMA-KJ_KOOR-S-P (Mengandung simbol ')
        (Evie, nomina), (Masamba, nomina), (dipercaya, verba), (membawakan, verba),
        (lagu, nomina), ('Berakit-akit, nomina), (', simbol), (,, td_koma),
        (diikuti, verba), (oleh, preposisi), (Andmesh, nomina), (dengan, dengan),
        ('Pelangi, nomina), (di, preposisi), (Matamu, nomina), (', simbol), (,, td_koma),
        (dan, konj_koor_tak_hingga), ('Maaf, nomina), (', simbol), (oleh, preposisi),
        (group, nomina), (musik, nomina), (A2L, nomina), (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<nomina>",
            "<verba>",
            "<verba>",
            "<nomina>",
            "<nomina>",
            "<simbol>",
            "<td_koma>",
            "<verba>",
            "<preposisi>",
            "<nomina>",
            "<dengan>",
            "<nomina>",
            "<preposisi>",
            "<nomina>",
            "<simbol>",
            "<td_koma>",
            "<kj_koor_tak_hingga>",
            "<nomina>",
            "<simbol>",
            "<preposisi>",
            "<nomina>",
            "<nomina>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_salah_konj_koor_tak_hingga_01(self):
        """
        -> Test: <kj_koor_tak_hingga> dua elemen menggunakan koma.
        (Polisi, nomina), (menemukan, verba), (pisau, nomina), (,, td_koma),
        (dan, konj_koor_tak_hingga), (senjata, nomina), (api, nomina),
        (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<verba>",
            "<nomina>",
            "<td_koma>",
            "<kj_koor_tak_hingga>",
            "<nomina>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertFalse(cfg_true_or_false(kal))

    def test_salah_konj_koor_terhingga_01(self):
        """
        -> Test: <kj_koor_terhingga> tdk menggunakan koma.
        (Polisi, nomina), (tiba, verba), (di, preposisi), (lokasi, nomina),
        (kejadian, nomina), (tetapi, konj_koor_terhingga), (pencuri, nomina),
        (tersebut, verba), (sudah, adverbia), (pergi, verba),
        (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<verba>",
            "<preposisi>",
            "<nomina>",
            "<nomina>",
            "<kj_koor_terhingga>",
            "<nomina>",
            "<verba>",
            "<adverbia>",
            "<verba>",
            "<td_akhir_kal>",
        ]
        self.assertFalse(cfg_true_or_false(kal))

    def test_salah_konj_koor_terhingga_klausa_01(self):
        """
        -> Test: <kj_koor_terhingga_klausa> tdk menggunakan koma.
        (Anak, nomina), (kecil, adjektiva), (pun, pun), (sudah, adverbia),
        (mengerti, verba), (apalagi, kj_koor_terhingga_klausa),
        (orang, nomina), (dewasa, adjektiva), (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<adjektiva>",
            "<pun>",
            "<adverbia>",
            "<verba>",
            "<kj_koor_terhingga_klausa>",
            "<nomina>",
            "<adjektiva>",
            "<td_akhir_kal>",
        ]
        self.assertFalse(cfg_true_or_false(kal))
