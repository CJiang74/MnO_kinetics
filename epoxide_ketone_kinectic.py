import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib.ticker import MultipleLocator, AutoMinorLocator

rcParams["axes.titleweight"] = "bold"
c_e = "#084191"
c_k = "#EF476F"
c_a = "#ffc857"
c_1 = "#FFD166"
c_2 = "#F72585"
c_3 = "#7209B7"
c_4 = "#3A0CA3"
c_5 = "#4361EE"
c_6 = "#4CC9F0"
error_kw = {"elinewidth": 2, "capsize": 5, "ecolor": "#abc4ff95"}


def plot_cyclopentene(df, potential, activity_water):
    df_cyclopentene = (
        df.loc[
            (df["potential"] == potential)
            & (df["catalyst"] == "MnO-0131")
            & (df["activity_water"] == activity_water)
        ]
        .groupby(["conc_cyclopentene", "catalyst"])
        .agg(
            {
                "Total_Current": ["mean", "std"],
                "FE_epoxide": ["mean", "std"],
                "FE_ketone": ["mean", "std"],
                "j_epoxide": ["mean", "std"],
                "j_ketone": ["mean", "std"],
            }
        )
        .reset_index()
    )
    fig, ax = plt.subplots()

    ax.errorbar(
        df_cyclopentene["conc_cyclopentene"],
        df_cyclopentene["j_epoxide"]["mean"],
        yerr=df_cyclopentene["j_epoxide"]["std"],
        fmt=".",
        label="Epoxide",
        c=c_e,
        markersize=15,
    )
    ax.errorbar(
        df_cyclopentene["conc_cyclopentene"],
        df_cyclopentene["j_ketone"]["mean"],
        yerr=df_cyclopentene["FE_ketone"]["std"],
        fmt=".",
        label="Ketone",
        c=c_k,
        markersize=15,
    )
    ax.set_ylabel("Current Density (mA/$cm^2$)", fontweight="bold")
    ax.set_xlabel("Cyclopentene Concentration (M)", fontweight="bold")
    ax.set_title(f"{potential} V vs.Fc/Fc$^+$, a$_w$ = {activity_water}")
    ax.set_ylim(0, 10)
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.legend(loc="upper left")
    ax.set_box_aspect(0.8)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"{x:.1f}"))

    return ax
def plot_water_activity(df, potential, conc_cyclopentene):
    df_water_activity = (
        df.loc[
            (df["potential"] == potential)
            & (df["catalyst"] == "MnO-0131")
            & (df["conc_cyclopentene"] == conc_cyclopentene)
        ]
        .groupby(["activity_water", "catalyst"])
        .agg(
            {
                "Total_Current": ["mean", "std"],
                "FE_epoxide": ["mean", "std"],
                "FE_ketone": ["mean", "std"],
                "j_epoxide": ["mean", "std"],
                "j_ketone": ["mean", "std"],
            }
        )
        .reset_index()
    )
    fig, ax = plt.subplots()
    ax.errorbar(
        df_water_activity["activity_water"],
        df_water_activity["j_epoxide"]["mean"],
        yerr=df_water_activity["j_epoxide"]["std"],
        fmt=".",
        label="Epoxide",
        c=c_e,markersize=15
    )
    ax.errorbar(
        df_water_activity["activity_water"],
        df_water_activity["j_ketone"]["mean"],
        yerr=df_water_activity["j_ketone"]['std'],
        fmt=".",
        label="Ketone",
        c=c_k,markersize=15
    )
    ax.set_ylabel("Current Density (mA/$cm^2$)", fontweight="bold")
    ax.set_xlabel("Water Activity", fontweight="bold")
    ax.set_title(f"{potential} V vs.Fc/Fc$^+$, {conc_cyclopentene} M cyclopentene")
    ax.set_ylim(0, 8)
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.legend (loc = "upper left")
    ax.set_box_aspect(0.8)
    #set y-axis tick label to have one decimal point
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"{x:.1f}"))
    return ax
