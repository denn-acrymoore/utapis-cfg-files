import nltk
from nltk.parse.chart import SteppingChartParser
from nltk.parse.chart import (
    FilteredBottomUpPredictCombineRule,
    LeafInitRule,
    FilteredSingleEdgeFundamentalRule,
    EmptyPredictRule,
    BottomUpPredictCombineRule,
    SingleEdgeFundamentalRule,
    BottomUpPredictRule,
)
import os

model_path = os.path.join(__file__, os.pardir, os.pardir)

grammar = nltk.data.load(
    "file:" + os.path.join(model_path, "utapis_sintaksis_kalimat_v2_skripsi.cfg"), "cfg"
)


# === Bottom-Up Chart Parser ===
# Test Finish Time (Pelengkap hanya bisa klausa lengkap): 60.643s
BU_STRATEGY = [
    LeafInitRule(),
    EmptyPredictRule(),
    BottomUpPredictRule(),
    SingleEdgeFundamentalRule(),
]

# === Bottom-Up Left-Corner Chart Parser ===
# Test Finish Time (Pelengkap bisa klausa tdk lengkap): 93.022s
# Test Finish Time (Pelengkap hanya bisa klausa lengkap): 36.355s
BU_LC_STRATEGY = [
    LeafInitRule(),
    EmptyPredictRule(),
    BottomUpPredictCombineRule(),
    SingleEdgeFundamentalRule(),
]

# === Left-Corner Chart Parser ===
# Test Finish Time (Pelengkap bisa klausa tdk lengkap): 74.112s
# Test Finish Time (Pelengkap hanya bisa klausa lengkap): 14.695s
LEFT_CORNER_STRATEGY = [
    LeafInitRule(),
    FilteredBottomUpPredictCombineRule(),
    FilteredSingleEdgeFundamentalRule(),
]

utapis_scp = SteppingChartParser(
    grammar=grammar, strategy=LEFT_CORNER_STRATEGY, trace=0
)


def stepping_chart_parsing(tags, scp):
    scp.initialize(tags)

    for step in scp.step():
        # Berhenti bila ditemukan parsing yang lengkap.
        if len(list(scp.parses())) > 0:
            break

        # Berhenti bila sudah tidak ada lagi kemungkinan parsing
        # yang bisa ditambahkan.
        if step is None:
            break

    # Print the result.
    # for x in scp.parses():
    #     print(x)
    #     break
    # print()

    # Return generator.
    return scp.parses()


def cfg_true_or_false(tags, scp=utapis_scp):
    generator = stepping_chart_parsing(tags, scp)
    generator_content_count = len(list(generator))
    if generator_content_count <= 0:
        return False
    else:
        return True
