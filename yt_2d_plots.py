# run from command line with
# streamlit run yt_2d_plots.py

import streamlit as st
import yt

st.title('yt 2d plotting in streamlit')

# load of the dataset, initial index build right away
# DO NOT USE yt.load_sample, it's hella slooooooow.
ds = yt.load("IsolatedGalaxy/galaxy0030/galaxy0030")
_ = ds.index

# function for creating a slice
def get_slice(axis, field, width, center_input):
    print('generating slice')


    valid_width = ds.quan(width, 'code_length')
    center = ds.domain_center.copy().to('code_length')
    center[ds.coordinates.axis_id[axis]] = center_input
    slc = yt.SlicePlot(ds, axis, field, width=valid_width, center=center)
    slc.render()
    return slc.plots[field].figure


# selections / settings
axis = st.selectbox('axis',
                 options = ds.coordinates.axis_order,
                 index = 0,
                 key='axis'
                  )
field_type = st.text_input('field_type', value="gas", key='field_type')
field_name = st.text_input('field_name', value="density", key='field_name')

width = st.slider('width (code_length)',
                  key='width',
                  min_value=0.0, max_value=1.0, value=1.0, step=0.01)
center = st.slider('center along normal (code_length)',
                     key='center',
                     value=0.5,
                     min_value=0.0, max_value=1.0, step=0.001,
                     format='%.6g'
                    )


# build initial figure
f = get_slice(st.session_state.axis,
             (st.session_state.field_type, st.session_state.field_name),
              st.session_state.width,
              st.session_state.center,
             )
the_figure = st.pyplot(f)
